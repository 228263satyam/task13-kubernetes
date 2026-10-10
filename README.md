# Task 13: Deploying Deep Learning Applications on Kubernetes

## CIFAR-10 Image Classification API using Docker and Kubernetes

## 📌 Project Overview

This project demonstrates how to deploy a trained deep learning model as a containerized web application using Docker and Kubernetes.

The application uses a trained **CIFAR-10 image classification model (`cifar10_model.keras`)** to predict the class of an uploaded image. A Flask REST API provides prediction and health-check endpoints. Docker packages the application, while Kubernetes manages deployment and exposes the API through a NodePort Service using Minikube.

## 🎯 Objectives

- Containerize a deep learning application using Docker.
- Deploy the containerized application on Kubernetes.
- Configure Kubernetes Deployment and Service manifests.
- Expose the application through a NodePort Service.
- Verify application health and image prediction.
- Monitor the deployment using Kubernetes commands.

## 🛠️ Technologies Used

- Python
- TensorFlow and Keras
- Flask
- Gunicorn
- Docker
- Kubernetes
- Minikube
- kubectl
- PowerShell

## 🏗️ Project Architecture

The application follows this workflow:

```text
User / Client
     |
     v
Flask REST API
     |
     v
Docker Container
     |
     v
Kubernetes Deployment
     |
     v
Kubernetes NodePort Service
     |
     v
CIFAR-10 Model Prediction
     |
     v
JSON Response
```

## 📁 Project Structure

```text
task13-kubernetes/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── cifar10_model.keras
├── README.md
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
└── Task_13_Kubernetes_Deployment_Report.pdf
```

The project report and Word document can also be included if required by the assignment.

## 🧠 CIFAR-10 Model

The application uses a previously trained Keras model to classify images into one of the following 10 classes:

1. Airplane
2. Automobile
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

The model file is named `cifar10_model.keras`.

## 🐳 Docker Setup

### Build the Docker image

Run the following command from the project root directory:

```powershell
docker build -t cifar10-api:v1 .
```

### Verify the image

```powershell
docker images
```

## ☸️ Kubernetes Deployment

This project uses Minikube to run Kubernetes locally.

### Step 1: Start Minikube

```powershell
minikube start
```

### Step 2: Load the Docker image into Minikube

```powershell
minikube image load cifar10-api:v1
```

### Step 3: Apply the Deployment manifest

```powershell
kubectl apply -f k8s/deployment.yaml
```

### Step 4: Apply the Service manifest

```powershell
kubectl apply -f k8s/service.yaml
```

### Step 5: Verify the deployment

```powershell
kubectl get deployments
kubectl get pods
kubectl get services
```

### Step 6: Check rollout status

```powershell
kubectl rollout status deployment/cifar10-deployment
```

### Step 7: Expose the application

```powershell
minikube service cifar10-service
```

This command provides a URL for accessing the application locally. Keep the terminal running while using the local tunnel URL.

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the API is running |
| GET | `/health` | Check application health |
| POST | `/predict` | Predict the class of an uploaded image |

### Homepage response

```json
{
  "message": "CIFAR-10 Deep Learning API is running"
}
```

### Health-check response

```json
{
  "status": "healthy"
}
```

### Image prediction response

Send a `POST` request to `/predict` using `multipart/form-data`, with the image attached under the field name `image`.

Example response:

```json
{
  "class_id": 0,
  "confidence": 0.461775,
  "prediction": "airplane"
}
```

The example above represents a prediction observed during testing. Results vary depending on the input image.

## 🧪 Testing the Prediction API

You can test the API using PowerShell and `curl.exe`:

```powershell
curl.exe -X POST `
  -F "image=@D:\path\to\test.jpg" `
  http://127.0.0.1:PORT/predict
```

Replace `D:\path\to\test.jpg` with the actual path to your image and `PORT` with the port from the URL printed by `minikube service cifar10-service`.

## 📊 Results

The following results were observed during implementation:

- Docker image successfully loaded into Minikube.
- Kubernetes Deployment successfully created.
- Kubernetes Service successfully exposed the API.
- Homepage endpoint returned a successful response.
- Health endpoint returned `healthy`.
- Image prediction endpoint returned a CIFAR-10 class prediction.
- Final deployment verification showed one ready replica.

## 🔧 Troubleshooting

### Pod is not ready

```powershell
kubectl describe pods
kubectl logs deployment/cifar10-deployment
```

### Restart the deployment

```powershell
kubectl rollout restart deployment/cifar10-deployment
kubectl rollout status deployment/cifar10-deployment
```

### Check the service

```powershell
kubectl get services
minikube service cifar10-service
```

TensorFlow may report that CUDA drivers are unavailable when running on a CPU-only environment. This is not necessarily a deployment failure.

## 📄 Project Report

The detailed report documents the application, Docker configuration, Kubernetes manifests, testing results, screenshots, troubleshooting, and conclusion.

**Report:** `Task_13_Kubernetes_Deployment_Report.pdf`

## 🎓 Learning Outcomes

Through this project, I learned how to:

- Deploy a trained deep learning model as a REST API.
- Package an application and its dependencies using Docker.
- Configure Kubernetes Deployments and Services.
- Expose an application using NodePort.
- Perform health checks and monitor pods.
- Troubleshoot container and health-probe issues.
- Test image inference through an HTTP API.

## 👨‍💻 Author

**Name:** Satyam Yadav

**Assignment:** Task 13 – Deploying Deep Learning Applications on Kubernetes

**Project Type:** Deep Learning Deployment / MLOps

---

*This project was developed for educational purposes as part of a deep learning deployment assignment.*
