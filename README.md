# LeadFlow Engine API: Event-Driven Lead Tracking & Process Automation Engine

**Developed by:** José Carlos Lobo  
**Main Stack:** Python | FastAPI | MySQL | SQLAlchemy | Pydantic  

---

## Language / Idioma

* For technical and architectural documentation: 👉 **[Read in English](#english-version)**
* Para el caso de estudio orientado a negocio: 👉 **[Leer en Español](#spanish-version)**

---

<div id="english-version"></div>

# English Version

## 🎯 Executive Summary & Business Value

LeadFlow Engine API is a production-ready backend system designed to manage corporate leads, business processes, and event-based workflows. Traditional CRM platforms only store the current, static state of a sales funnel or dynamic pipeline, completely wiping away previous actions. LeadFlow resolves this structural limitation by managing actions as a continuous event matrix — enabling 100% process visibility, automated behavior, and reliable business auditing.

### 🏢 Real-World Use Cases:
* Lead Generation Pipelines: Streamlining information from raw web scraping extraction into verified sales funnels.
* Enterprise CRM Backends: Supporting multi-department customer relation architectures.
* Automation Triggers: Sending follow-up actions and automated responses based on step transitions.
* AI Agent Architectures: Serving as an optimized operational registry for automated AI business processing agents.

---

## 🔥 Key Features & Technical Assets

* Comprehensive Client Governance: Structured management of companies and client entities.
* Event-Driven Status Lifecycle: Instead of manually overwriting states (e.g., status = "contacted"), every single action saves as an independent immutable event entity (contacted -> follow_up -> closed).
* Instant Audit Logs: Reconstructed complete history logs available for corporate analysis and bottleneck detection.
* High Performance Data Models: Built on decoupled entities (Clients, Processes, Process Events) using relational mappings.

---

## ⚙️ Architecture Design

The engine follows clean layered architecture patterns to support isolation and scalability:

Esquema de Arquitectura:
API (FastAPI) -> Schemas (Pydantic validation) -> Services (business logic) -> Repositories (data access) -> Database (MySQL)

---

## 🚀 Getting Started & Local Setup

### Prerequisites
* Python 3.10+
* MySQL Instance

### 1. Environment Deployment
Comandos para ejecutar en consola:
git clone https://github.com/JCarlosWolf/leadflow-engine-api.git
cd leadflow-engine-api
python -m venv .venv

* Activar entorno virtual:
Windows: .venv\Scripts\activate
Linux/macOS: source .venv/bin/activate

Instalar dependencias:
pip install -r requirements.txt

### 2. Configuration (.env)
Create a .env file in the root folder:
PROJECT_NAME=LeadFlow Engine API
API_V1_STR=/api/leadflow
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=leadflow_db

### 3. Database Initialization
Ejecuta las directivas internas para preparar el esquema:
python -c "from app.db.init_db import init_db; init_db()"

### 4. Run Server
uvicorn app.main:app --reload

Interactive Swagger Documentation: http://localhost:8000/docs

---

## 📡 Key Endpoint Context

* GET /api/leadflow/processes/{process_id}/full
Single composite endpoint that automatically queries, bundles, and delivers the full transactional landscape: the active process context, associated client entity, and the complete event timeline history in a unified payload.

---

## 📬 Contact & Process Consulting

* Developer: José Carlos Lobo
* Specialty: Event-Driven Software, Secure API Architectures, & Corporate Process Optimization.
* LinkedIn: www.linkedin.com/in/josé-carlos-lobo-473b458a

---
---

<div id="spanish-version"></div>

# Versión en Español: Caso de Estudio de Negocio

## 🎯 ¿Qué es LeadFlow Engine? (Perspectiva de Negocio)

En el mercado corporativo actual, la mayoría de los sistemas CRM tradicionales cometen un error crítico de diseño: solo guardan el "estado actual" de un cliente potencial o lead, destruyendo todo el historial de interacciones pasadas. Si un registro pasa de "Contactado" a "Perdido", se pierde para siempre la visibilidad de cuántas llamadas tomó el proceso, quién intervino y cuánto tiempo real se consumió en cada etapa.

LeadFlow Engine es una API backend de nivel de producción diseñada bajo una arquitectura dirigida por eventos (Event-Driven). Su propósito central es que cada hito comercial, actualización o intervención humana se guarde como un evento inmutable en el sistema. Esto no solo genera una bitácora de auditoría infalible, sino que permite desencadenar automatizaciones inteligentes cada vez que ocurre una transición en el negocio.

### 🏢 Casos de Uso Reales en la Empresa:
* Automatización de Embudos de Venta: Conexión directa con sistemas de extracción de datos (web scraping) para inyectar leads y procesarlos sin intervención humana.
* Backends para CRM Corporativos: Estructura robusta para centralizar la gestión de múltiples departamentos y cuentas de clientes.
* Disparadores de Acciones Automáticas: Envío automatizado de correos de seguimiento, alertas internas o reasignación de tareas al cambiar el estado de un lead.

---

## 🚀 Características Clave y Valor Empresarial

* Arquitectura Basada en Eventos: El ciclo de vida operativo del lead avanza de forma lógica mediante eventos correlacionados (Contactado -> Seguimiento -> Cerrado con Éxito), manteniendo un rastro de auditoría transparente y continuo.
* Reducción Absoluta del Error Humano: Validaciones de datos de entrada estrictas mediante modelos Pydantic, garantizando la integridad de los datos financieros y de contacto antes de guardarse en la base de datos MySQL.
* Vista Consolidada de un Solo Clic: Endpoint integrado diseñado para analistas que devuelve de golpe toda la información del cliente, el estado del proceso y su línea de tiempo histórica en una única consulta de alta velocidad.
* Diseño Limpio y Altamente Escalable: Separación rigurosa de responsabilidades (Capas de API, Lógica de Negocio y Persistencia) asegurando que el mantenimiento del software sea económico y fácil a largo plazo.

---

## ✉️ Contacto y Consultoría de Automatización

* Desarrollador: José Carlos Lobo
* LinkedIn: www.linkedin.com/in/josé-carlos-lobo-473b458a
