/** @odoo-module */
import { templates } from "@web/core/assets";
import { Component, mount, whenReady, onWillStart, useState } from "@odoo/owl";

export class Events extends Component {
    static template = "custom_event.events"
    setup() {
        onWillStart(this.onWillStart)
        this.events = useState([])
    }
    async onWillStart() {
        let response = await fetch('/api/events', {
            method: "GET",
            headers: {
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
        },);
        response = await response.json()
        this.events = response.events
    }
}

whenReady(() => {
    let $selector = document.querySelector(".custom_events")
    if ($selector) {
        mount(Events, $selector, { templates });
    }
});
