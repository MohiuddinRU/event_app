/** @odoo-module */
import {templates} from "@web/core/assets";
import {Component, mount, whenReady} from "@odoo/owl";

export class Events extends Component {
    static template = "custom_event.events"
    setup() {
        console.log('hello world')
    }
}

whenReady(() => {
    let $selector = document.querySelector(".custom_events")
    console.log("$selector = ", $selector)
    mount(Events, $selector, {templates});
});
