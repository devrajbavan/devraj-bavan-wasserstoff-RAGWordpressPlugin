# RAG-Based Query Suggestion Chatbot with Chain of Thought for WordPress Sites

## Project Overview

This project involves developing a versatile, intelligent chatbot that utilizes a Retrieval-Augmented Generation (RAG) system enhanced with a Chain of Thought (CoT) strategy. The chatbot is designed to integrate seamlessly into various WordPress blogs and sites, adapting to a wide range of topics while maintaining logical and contextually relevant interactions.

## Table of Contents

- [System Design](#system-design)
  - [Requirement Analysis](#requirement-analysis)
  - [Architecture Design](#architecture-design)
- [Implementation](#implementation)
  - [WordPress Data Retrieval and Embedding Generation](#wordpress-data-retrieval-and-embedding-generation)
  - [RAG Setup and Chain of Thought Integration](#rag-setup-and-chain-of-thought-integration)
- [Integration with WordPress](#integration-with-wordpress)
- [Testing and Evaluation](#testing-and-evaluation)
- [Documentation and Reporting](#documentation-and-reporting)
- [Deliverables](#deliverables)
- [Evaluation Benchmark](#evaluation-benchmark)
- [Requirements](#requirements)

## System Design

### Requirement Analysis

**Objective:** Create a chatbot that adapts its interaction style and content based on the specific WordPress site it is deployed on.

**Actions:**
- Perform an analysis of typical user queries and interactions across a range of blogs to gather diverse requirements.
- Design user interaction flows that guide users through their queries using a series of contextually relevant questions, enhanced by a logical chain of thought.

### Architecture Design

**Objective:** Build a scalable and efficient system capable of real-time data retrieval, processing, and dynamic response generation.

**Components:**
- **Data Retrieval:** Utilize WordPress APIs to fetch real-time content updates.
- **Embedding Generator:** Convert textual content into vector embeddings using models like Sentence-BERT.
- **Vector Database:** Employ a system like Faiss to store and retrieve embeddings efficiently.
- **RAG Processor:** Integrate RAG to generate responses based on retrieved information.
- **Chain of Thought Module:** Develop this module to enhance the RAG outputs with logical progression and context continuity.
- **User Interface:** Design an interactive chat interface that can dynamically display the chatbot’s thought process.

## Implementation

### WordPress Data Retrieval and Embedding Generation

**Real-Time Data Fetching:** Implement hooks and REST API calls within WordPress to fetch new and updated content.

**Pseudocode for Embedding Update:**
```python
def update_embeddings_on_new_post(post):
    text = extract_text(post)
    embeddings = generate_embeddings(text)
    update_vector_database(post.id, embeddings)
