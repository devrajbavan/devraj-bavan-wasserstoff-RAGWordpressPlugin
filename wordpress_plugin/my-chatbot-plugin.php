<?php
/*
Plugin Name: My Chatbot Plugin
Description: A plugin to integrate the RAG-based chatbot with WordPress.
Version: 1.0
Author: Your Name
*/

function enqueue_my_chatbot_scripts() {
    wp_enqueue_script('my-chatbot-script', plugin_dir_url(__FILE__) . 'my-chatbot.js', array('jquery'), '1.0', true);
    wp_localize_script('my-chatbot-script', 'my_chatbot_ajax', array(
        'ajax_url' => admin_url('admin-ajax.php')
    ));
}
add_action('wp_enqueue_scripts', 'enqueue_my_chatbot_scripts');

function handle_chatbot_query() {
    $question = sanitize_text_field($_POST['question']);
    $response = wp_remote_post('http://your-flask-app-url/get_answer', array(
        'body' => json_encode(array('question' => $question)),
        'headers' => array('Content-Type' => 'application/json')
    ));
    if (is_wp_error($response)) {
        wp_send_json_error($response->get_error_message());
    } else {
        wp_send_json_success(json_decode(wp_remote_retrieve_body($response)));
    }
}
add_action('wp_ajax_nopriv_my_chatbot_query', 'handle_chatbot_query');
add_action('wp_ajax_my_chatbot_query', 'handle_chatbot_query');
?>
