Entrypoint script to trigger the whole engine.
from app.engine.playbook_runner import run_playbook, load_incident

incident = load_incident("app/incidents/sample_incident.json")
run_playbook("app/playbooks/azure-unauthorized-vm-login.yml", incident)
Run it with:
python3 run_azure_playbook.py
