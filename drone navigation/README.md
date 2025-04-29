# 🚁 Follow-Me Drone API – FastAPI Deployment

This project simulates the behavior of an autonomous **Follow-Me Drone** using a lightweight and deployable **FastAPI-based web service**.  
The API receives real-time movement commands (like "up", "left", "forward") and returns simulated drone actions, acting as a backend controller for drone navigation logic.

It is ideal for demonstrating drone command control logic, IoT integrations, and deploying machine learning-enabled drone modules in real-world applications.

---

## ✨ Features
- ✅ Built using **FastAPI** – high performance & easy to deploy.
- ✅ Supports drone movement commands via RESTful API.
- ✅ Easy to extend with real drone control, object detection, or reinforcement learning.
- ✅ Ready for deployment on **Render**, **Hugging Face Spaces**, or **AWS**.

---

## 🔧 API Endpoints

### `GET /`
> Health check endpoint  
**Response:** 
```json
{ "message": "Follow-Me Drone API is up and running!" }
```

### `POST /move-drone/`
> Send a movement command to the drone

**Request JSON**:
```json
{ "direction": "up" }
```

**Valid directions**: `up`, `down`, `left`, `right`, `forward`, `backward`

**Successful Response**:
```json
{ "status": "success", "action": "Drone is moving up" }
```

**Invalid Direction Response**:
```json
{ "status": "error", "message": "Invalid direction. Please use up, down, left, right, forward, or backward." }
```

---

## 🚀 Quick Start

1. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2. **Run the server**:
    ```bash
    uvicorn app:app --host 0.0.0.0 --port 8000
    ```

3. **Test API**:
    - Open browser at [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.
    - Or use `curl`:
      ```bash
      curl -X POST "http://localhost:8000/move-drone/" -H "Content-Type: application/json" -d '{"direction": "forward"}'
      ```

---

## 🛰️ Use Cases
- Autonomous drone navigation backend
- Testing RL-based drone simulations
- Smart surveillance systems
- IoT Drone command API

---

## 🛠️ Tech Stack
- Python 3.9+
- FastAPI
- Uvicorn (ASGI server)
- Pydantic (for data validation)

---

## 📄 License
This project is open-source under the [MIT License](LICENSE). Feel free to use and modify it!

---

## ✨ Author
**Your Name Here**  
*Developed for Drone Simulation and FastAPI Deployment Practice.*

---