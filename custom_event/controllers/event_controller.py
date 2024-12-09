from odoo import http
from odoo.http import request, Response
import json


class EventController(http.Controller):
    @http.route("/api/events", type="json", auth="user", methods=["POST"])
    def create_event(self, **kwargs):
        try:
            event = request.env["event.event"].create(kwargs)
            return {
                "status": "success",
                "event": event.read(),
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
            }

    @http.route("/api/events/<int:event_id>", type="json", auth="user", methods=["GET"])
    def read_event(self, event_id):
        event = request.env["event.event"].browse(event_id)
        if not event.exists():
            return {
                "status": "error",
                "message": "Event not found",
            }
        return {
            "status": "success",
            "event": event.read(),
        }

    @http.route("/api/events", type="http", auth="user", methods=["GET"])
    def list_events(self, **kwargs):
        page_number = int(kwargs.get("page[number]", 1))
        page_size = int(kwargs.get("page[size]", 10))

        offset = (page_number - 1) * page_size
        events = request.env["event.event"].sudo().search([], limit=page_size, offset=offset)

        response =  json.dumps({
            "status": "success",
            "events": events.sudo().read(["title", "location", "date"]),
            "pagination": {
                "page_number": page_number,
                "page_size": page_size,
                "total": request.env["event.event"].sudo().search_count([]),
            },
        }, default=str)

        return response

    @http.route("/api/events/<int:event_id>", type="json", auth="user", methods=["PUT"])
    def update_event(self, event_id, **kwargs):
        """Update an existing event by ID."""
        event = request.env["event.event"].browse(event_id)
        if not event.exists():
            return {
                "status": "error",
                "message": "Event not found",
            }

        try:
            event.write(kwargs)
            return {
                "status": "success",
                "event": event.read(),
            }
        except Exception as e:
            return {
                "status": "error",
                "message": str(e),
            }

    @http.route(
        "/api/events/<int:event_id>", type="json", auth="user", methods=["DELETE"]
    )
    def delete_event(self, event_id):
        """Delete an event record by ID."""
        event = request.env["event.event"].browse(event_id)
        if not event.exists():
            return {
                "status": "error",
                "message": "Event not found",
            }

        event.unlink()
        return {
            "status": "success",
            "message": "Event deleted",
        }
