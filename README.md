# AI Thumbnail Generator

An AI-powered full-stack application that generates high-quality thumbnails using modern AI workflows, real-time backend processing, and cloud-based image optimization.

Built with FastAPI, React, OpenAI APIs, ImageKit, and SQLModel to provide an efficient and scalable thumbnail generation experience.

---

## Overview

This project allows users to upload images, provide custom prompts or styles, and generate AI-powered thumbnails dynamically. The system integrates AI image generation, cloud media storage, asynchronous backend processing, and real-time status updates into a modern API-driven workflow.

The application is designed to demonstrate practical backend engineering concepts including REST API development, async processing, media handling, external API integrations, and structured database management.

---

## Key Features

- AI-powered thumbnail generation using OpenAI APIs
- FastAPI-based RESTful backend architecture
- Real-time progress updates using Server-Sent Events (SSE)
- Cloud image storage and optimization with ImageKit
- Async request handling for improved responsiveness
- Structured database models using SQLModel
- Prompt-based thumbnail customization
- Image upload and transformation workflows
- Clean modular backend structure

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLModel
- SQLite

### Frontend
- React
- Vite

### AI & Cloud Services
- OpenAI API
- ImageKit

### Tools & Utilities
- Postman
- Git & GitHub

---

## System Workflow

1. User uploads an image and provides a custom thumbnail prompt.
2. The backend uploads and stores media using ImageKit.
3. FastAPI processes the request and manages generation workflows.
4. OpenAI APIs generate AI-based thumbnail outputs.
5. Real-time status updates are streamed using SSE.
6. Optimized images are returned to the frontend for preview and usage.

---

## Project Structure

```bash
ai-thumbnail-generator/
│
├── backend/
│   ├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   └── main.py
│
├── frontend/
│   ├── src/
│   └── public/
│
├── README.md
├── requirements.txt
└── .env.example
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/kushagranayak55-web/ai-thumbnail-generator.git
```

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## Learning Outcomes

This project helped in understanding:

- REST API development with FastAPI
- AI API integration workflows
- Async backend processing
- Database modeling using SQLModel
- Real-time communication using SSE
- Cloud-based media management
- Full-stack application architecture

---

## Status

Currently under active development and improvements.

---

## Author

Kushagra Nayak

LinkedIn:
https://www.linkedin.com/in/kushagra-nayak-99786a305

GitHub:
https://github.com/kushagranayak55-web
