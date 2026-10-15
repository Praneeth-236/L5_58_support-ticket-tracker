"""Manage support tickets and persist them as JSON."""

import json
import logging
from pathlib import Path

TICKETS = {}
AUDIT_LOG = []


def create_ticket(
    title,
    description,
    reporter,
    priority="medium",
    category="general",
):
    """Create and store a support ticket."""
    if not title:
        return None

    ticket_id = str(len(TICKETS) + 1)
    ticket = {
        "id": ticket_id,
        "title": title,
        "description": description,
        "priority": priority,
        "category": category,
        "status": "open",
        "reporter": reporter,
        "assignee": None,
    }
    TICKETS[ticket_id] = ticket
    AUDIT_LOG.append(f"Created ticket {ticket_id} for {reporter}")
    return ticket


def assign_ticket(ticket_id, agent):
    """Assign a ticket to an agent."""
    try:
        TICKETS[ticket_id]["assignee"] = agent
    except KeyError:
        return False
    return True


def update_status(ticket_id, status):
    """Update a ticket's status."""
    if ticket_id not in TICKETS:
        return None

    TICKETS[ticket_id]["status"] = status
    return TICKETS[ticket_id]


def search_tickets(status=None, priority=None):
    """Search tickets by optional status and priority."""
    results = []

    for ticket in TICKETS.values():
        if status is not None and ticket["status"] != status:
            continue
        if priority and ticket["priority"] != priority:
            continue
        results.append(ticket)

    return results


def save_tickets(path="tickets.json"):
    """Save tickets to a JSON file."""
    with Path(path).open("w", encoding="utf-8") as file:
        json.dump(TICKETS, file, indent=2)


def load_tickets(path="tickets.json"):
    """Load tickets from a JSON file."""
    with Path(path).open("r", encoding="utf-8") as file:
        loaded_tickets = json.load(file)

    TICKETS.clear()
    TICKETS.update(loaded_tickets)


def print_ticket_report():
    """Print a summary of all tickets."""
    print("Support Tickets")

    if not TICKETS:
        print("No tickets yet")

    for ticket_id, ticket in TICKETS.items():
        print(ticket_id, ticket["title"], ticket["status"])


def close_ticket(ticket_id):
    """Close a ticket if it exists."""
    if ticket_id not in TICKETS:
        return False

    TICKETS[ticket_id]["status"] = "closed"
    return True


def is_open(ticket_id):
    """Return whether a ticket is open or in progress."""
    if ticket_id not in TICKETS:
        return False

    return TICKETS[ticket_id]["status"] in ("open", "in_progress")


def main():
    """Run the support-ticket tracker demonstration."""
    logging.basicConfig(level=logging.INFO)

    create_ticket(
        "Cannot sign in",
        "Password reset link fails",
        "alex@example.com",
    )
    create_ticket(
        "Billing question",
        "Charged twice",
        "lee@example.com",
        priority="high",
    )

    assign_ticket("1", "agent-01")
    update_status("1", "in_progress")
    print_ticket_report()

    logging.info("Tickets created: %s", len(TICKETS))
    print("Ticket 1 open?", is_open("1"))

    ticket_id = input("Ticket id to close (Enter to skip): ")
    if ticket_id and not close_ticket(ticket_id):
        print(f"Ticket {ticket_id} not found")

    save_tickets()


if __name__ == "__main__":
    main()
