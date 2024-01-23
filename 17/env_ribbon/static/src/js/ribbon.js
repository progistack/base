/** @odoo-module **/

import { useBus, useService } from "@web/core/utils/hooks";
import { Component, xml } from "@odoo/owl";
import {registry} from "@web/core/registry";


export class WebEnvironmentRibbon extends Component {
    setup() {
        super.setup(...arguments);
        this.orm = useService("orm");
        useBus(this.env.bus, "WEB_CLIENT_READY", this.showRibbon.bind(this));
    }

    showRibbon() {
        const ribbon = $(".env-ribbon");
        const self = this;
        ribbon.hide();
        // Get ribbon data from backend
        self.orm.call("web.environment.ribbon.backend", "get_environment_ribbon").then(function (ribbon_data) {

            ribbon.removeClass("env-ribbon-TR");
            ribbon.addClass("env-ribbon-TR");

            // Ribbon name
            if (ribbon_data.name && ribbon_data.name !== "False") {
                ribbon.html(ribbon_data.name);
                ribbon.show();
            }
            // Ribbon color
            if (ribbon_data.color && self.validStrColour(ribbon_data.color)) {
                ribbon.css("color", ribbon_data.color);
            }
            // Ribbon background color
            if (
                ribbon_data.background_color &&
                self.validStrColour(ribbon_data.background_color)
            ) {
                ribbon.css("background-color", ribbon_data.background_color);
            }
        });
    }

    validStrColour(strToTest) {
        if (strToTest === "") {
            return false;
        }
        if (strToTest === "inherit") {
            return true;
        }
        if (strToTest === "transparent") {
            return true;
        }
        var image = document.createElement("img");
        image.style.color = "rgb(0, 0, 0)";
        image.style.color = strToTest;
        if (image.style.color !== "rgb(0, 0, 0)") {
            return true;
        }
        image.style.color = "rgb(255, 255, 255)";
        image.style.color = strToTest;
        return image.style.color !== "rgb(255, 255, 255)";
    }
};

WebEnvironmentRibbon.props = {};
WebEnvironmentRibbon.template = xml`<div class="env-ribbon" />`;

registry.category("main_components").add("WebEnvironmentRibbon", {
    Component: WebEnvironmentRibbon,
});
