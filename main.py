from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="ApexFlow API")

class WorkflowRequest(BaseModel):
    task_name: str
    parameters: dict = {}

@app.get("/")
def read_root():
    return {"status": "ok", "message": "ApexFlow Automator is running"}

@app.post("/run-workflow")
def run_workflow(request: WorkflowRequest):
    # Aquí iría la lógica real de tu automatización
    if not request.task_name:
        raise HTTPException(status_code=400, detail="Task name is required")
    
    # Simulamos la ejecución exitosa de la tarea
    result = {
        "task": request.task_name,
        "status": "completed",
        "details": f"Workflow '{request.task_name}' executed successfully.",
        "parameters_received": request.parameters
    }
    return result