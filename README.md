# EventHub - Advanced Event Booking API

EventHub is a robust, production-ready RESTful API designed for event management and ticket reservation systems. It serves as a backend solution capable of handling high-concurrency booking requests while ensuring data integrity.

This project demonstrates a professional implementation of Django REST Framework, focusing on clean architecture, security, and scalable database interactions.

## 🚀 Key Features

### 1. User Management & Authentication
*   **Custom User Model:** Extends `AbstractBaseUser` for flexibility and scalability.
*   **JWT Authentication:** Secure, stateless authentication using `SimpleJWT` (Access & Refresh tokens).
*   **Role-Based Access:** Distinction between Organizers, Attendees, and Admins.

### 2. Event Management
*   **Comprehensive CRUD:** Organizers can create, update, and manage events.
*   **Dependency Injection:** Automatic injection of the logged-in user as the event organizer (Backend-driven logic).
*   **Categorization:** Hierarchical category system for better event discovery.
*   **Advanced Filtering:** Powerful filtering, searching, and sorting capabilities (using `django-filter`).

### 3. Ticket & Booking System (The Core)
*   **Multi-Type Tickets:** Support for various ticket classes per event (VIP, Regular, Early Bird).
*   **Inventory Management:** Real-time tracking of ticket capacity.
*   **Order Processing:** Secure calculation of totals on the server-side (Client input validation).

### 4. Technical Excellence
*   **Concurrency Control:** Prevents **Race Conditions** during high-traffic ticket sales using Database Locks (`select_for_update`) and Atomic Transactions.
*   **UUIDs:** Usage of UUIDs for Primary Keys to ensure security and prevent ID enumeration attacks.
*   **API Documentation:** Auto-generated, interactive API documentation via **Swagger/OpenAPI** (`drf-spectacular`).

---

## 🛠 Tech Stack

*   **Language:** Python 3.10+
*   **Framework:** Django 4.2+
*   **API Toolkit:** Django REST Framework (DRF)
*   **Database:** PostgreSQL (Production grade)
*   **Dependency Manager:** Poetry
*   **Documentation:** OpenAPI 3.0 (Swagger UI & Redoc)
*   **Security:** JWT, Flake8, Black

---

## 🏗 Project Architecture

The project follows a modular "Monolithic" architecture, designed for easy transition to microservices if needed:

*   **`core`**: Contains abstract base models (UUIDs, timestamps) and shared utilities.
*   **`users`**: Handles custom user logic and authentication.
*   **`events`**: Manages event data, categories, and organizer logic.
*   **`tickets`**: Handles the business logic for ticket definitions, orders, and inventory.

---

## ⚡ Concurrency & Data Integrity

One of the main challenges in booking systems is **Overselling** (selling more tickets than available capacity) when multiple users attempt to buy the last ticket simultaneously.

**EventHub solves this by implementing:**
1.  **Atomic Transactions:** ensuring the "payment" and "inventory deduction" happen as a single unit of work.
2.  **Row-Level Locking:** Using `select_for_update()` to lock the specific ticket row in the database during the purchase process. This forces concurrent requests to wait until the transaction is complete, guaranteeing 100% data accuracy.

---

## 📚 API Documentation

The project includes fully interactive documentation. Once the server is running, you can explore the endpoints at:

*   **Swagger UI:** `/api/schema/swagger-ui/`
*   **Redoc:** `/api/schema/redoc/`

---

## 🧪 Testing

The project includes comprehensive **Integration Tests** covering:
*   Authentication flows.
*   Event creation logic.
*   Purchase flows and inventory updates.
*   **Race condition simulation** and overselling prevention.