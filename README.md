# Food Delivery ETA Prediction System 🧭⏱️

This repository encapsulates an end-to-end ML system architected for high-precision food delivery time (ETA) forecasting. The system integrates principled data preprocessing, experimental methodology, ensemble modeling, automated pipeline orchestration, and containerized deployment infrastructure.

---

## 🔍 Problem Domain

In the on-demand logistics domain, time precision is a first-class citizen. Accurate ETA (Estimated Time of Arrival) estimation affects:
- **Customer experience** (trust and retention),
- **Fleet management** (operational efficiency),
- **Resource optimization** (cost reduction in high-traffic nodes).

This project simulates a Swiggy-like environment to build an **ML-driven delivery time inference engine**, optimizing prediction accuracy over heterogeneous delivery contexts.

---

## 🎯 Objective

Design and operationalize a machine learning pipeline that generalizes well over:
- Urban mobility variability (city_type, traffic, vehicle_condition),
- Contextual temporal patterns (order_time_of_day, is_weekend, festival),
- Service constraints (multiple_deliveries, type_of_order, ratings),
- Geospatial logistics (pickup_time_minutes, distance).

---

## 🧪 Modeling Strategy Overview

1. **Missing Data Strategy**  
2. **Model Benchmarking & Selection**  
3. **Hyperparameter Search & Optimization**  
4. **Stacked Ensemble Integration**

---

## 📊 Feature Schema

| Feature Name            | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| `age`                   | Driver or account tenure; proxy for experience                             |
| `ratings`               | Historical service quality, indicating behavioral patterns                 |
| `pickup_time_minutes`   | Latency between order placement and pickup                                 |
| `distance`              | Geodesic or route-based delivery path length                               |
| `weather`               | Encoded climatic category; affects delivery friction                       |
| `type_of_order`         | Categorical: food class or preparation intensity                           |
| `type_of_vehicle`       | Mode of delivery (bike, scooter, etc.)                                     |
| `festival`              | Binary indicator of peak-demand seasonality                                |
| `city_type`             | Urban classification (metro, tier-2, etc.)                                 |
| `is_weekend`            | Binary flag for weekend status                                              |
| `order_time_of_day`     | Time block encoding (morning, lunch, dinner, late night)                   |
| `traffic`               | Congestion proxy; ordinal or sensor-based input                            |
| `vehicle_condition`     | Maintenance score or categorical proxy (new, moderate, old)                |
| `multiple_deliveries`   | Number of concurrent deliveries being handled by the same delivery agent   |

---

## 🧱 System Design & Engineering

### 🔁 **Pipeline Automation: DVC**
- Encodes deterministic ML workflows via `dvc.yaml`.
- Stages include: preprocessing → training → evaluation → model registry.
- Outputs logged and version-controlled via DagsHub.

### ☁️ **Cloud-Backed Storage: AWS S3**
- Artifacts (datasets, models) pushed to S3 using secure, programmatic access.
- Enables scalable remote storage and pipeline portability.

### 📈 **Experiment Tracking: DagsHub**
- Central hub for:
  - Experiment metric comparison,
  - Model performance visualization,
  - Commit-wise provenance tracking.

### 🧪 **CI/CD: GitHub Actions**
- Triggered on pull requests or commits to `main`.
- Validates:
  - Code correctness,
  - DVC pipeline integrity,
  - Docker image build success,
  - FastAPI application health checks.

### 🐳 **Containerization: Docker**
- Ensures environment reproducibility.
- Production-grade FastAPI app encapsulated for lightweight serving.

---

## 🧠 Model Performance

- **Final Model**: StackingRegressor (LGBM + RandomForest)
- **Accuracy**: ~85% (R² Score)
- **Error Distribution**: Majority predictions within ±5 min deviation
- **Inference Speed**: ~20ms per sample on CPU

---

## 📌 Architectural Highlights

- Modular project layout using a cookiecutter template.
- Reproducible pipeline runs via DVC with data provenance.
- Metrics and model lineage tracked visually in DagsHub.
- End-to-end automation from data versioning to deployment pipeline.
- Dockerized REST API for low-latency predictions.

---

## 📚 Lexicon of Advanced Terms

- **Stacked Generalization**: Ensemble strategy that learns a meta-model from base model predictions to minimize generalization error.
- **Data Provenance**: Recording the lineage and transformations of data across the ML lifecycle.
- **Pipeline DAG**: Directed Acyclic Graph of pipeline stages, ensuring immutable, traceable model training processes.
- **CI/CD in MLOps**: Continuous Integration for data science code, and Continuous Delivery for pipeline re-runs, model validation, and container redeployment.
- **Entropy-based Modeling**: Algorithms like LGBM utilize gain (information entropy) to optimize tree splitting for tabular data.

---

## 🔚 Summary

This project exemplifies the convergence of rigorous data science, software engineering discipline, and cloud-native infrastructure to deliver a resilient and scalable delivery ETA prediction system. From hypothesis-driven feature engineering to LGBM-stacked inference pipelines, it brings forth a deployable ML product ecosystem, suitable for enterprise-grade logistics systems.

---

