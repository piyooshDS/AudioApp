/*
# cpanel12 - user_preferences.js             Copyright(c) 1997-2014 cPanel, Inc.
#                                                           All Rights Reserved.
# copyright@cpanel.net                                         http://cpanel.net
# This code is subject to the cPanel license. Unauthorized copying is prohibited
*/

/* global SetNvData: false, NVData: false,
    $: false */
/* jshint -W064 */

(function(){
    /**
     * Sets the user preferences tutorial in NVData and hides the tutorial
     * @param  {Element} container The tutorial container to be hidden
     */
    function completeTutorial(container){
        SetNvData("hideUserPreferencesOverlay", 1, handleSetNvData);
        container.addClass("hidden");
        $("#content").removeClass("overlay-mask");
    }

    /**
     * Sets the default_webmail_app in NVData
     * @param  {String} client
     */
    function setDefault(client){
        if(client && client.length > 0) {
            if(window.NVData["default_webmail_app"] !== client) {
                SetNvData("default_webmail_app", client, handleSetNvData);
            } else {
                selectDefault(client);
            }
        }
    }

    /**
     * Update the default mail client on both user dropdown and on index page.
     * @param  {object} evt
     */
    function updateDefaultHandler(evt) {
        if (typeof selectDefault !== "undefined" && $.isFunction(selectDefault)) {
            selectDefault(evt.client);
        }

        if(typeof updateDefaultSelection !== "undefined" && $.isFunction(updateDefaultSelection)) {
            updateDefaultSelection();
        }
    }

    // bind custom event to the document body
    $(document.body).bind("updateDefault", updateDefaultHandler);

    /**
     * Select default mail client in the user dropdown
     * @param  {String} client default webmail client
     */
    function selectDefault(client){
        $("span[data-default-webmail-app]").each(function(){
            var mailClient = $(this);
            if(mailClient.attr("data-default-webmail-app") === client) {
                mailClient.removeClass("fa-star-o fa-spinner fa-spin").addClass("fa-star");
            } else {
                mailClient.removeClass("fa-star fa-spinner fa-spin").addClass("fa-star-o");
            }
        });
    }

    /**
    * Set the loading indicator in the user dropdown
    */
    function setLoadingIndicator(client) {
        var mailClientImg = $("span[data-default-webmail-app=" + client + "]");
        mailClientImg.removeClass("fa-star-o").addClass("fa-spinner fa-spin").removeClass("fa-star");
    }


    /**
     * Callback after setting the NVData
     * @param  {Object} data data returned from SetNvData method
     */
    function handleSetNvData(data) {
        if(data) {
            window.NVData["default_webmail_app"] = NVData["default_webmail_app"];

            $.event.trigger({
                type: "updateDefault",
                client: NVData["default_webmail_app"]
            });
        }
    }

    /*
    * Updates the default selection on the mailclient template
    */
    function updateDefaultSelection() {
        $("#mailClientList .panel").each(function() {
            if($(this).attr("data-default-webmail-app") === NVData["default_webmail_app"]) {
                $(this).removeClass("panel-default").addClass("panel-primary");
                $(this).children("a.mail-client-action-link").removeClass("show").addClass("hide");
                $(this).find(".default-mail-client").removeClass("hide").addClass("show");
            } else {
                $(this).removeClass("panel-primary").addClass("panel-default");
                $(this).children("a.mail-client-action-link").removeClass("hide").addClass("show");
                $(this).find(".default-mail-client").removeClass("show").addClass("hide");
            }
        });
    }

    $(function(){
        var client = window.NVData["default_webmail_app"] || "";

        selectDefault(client);

        // user preferences dropdown
        $("a.app-fav").click(function(event){
            var client = $(this).attr("data-default-webmail-app");
            setLoadingIndicator(client);
            setDefault(client);
            event.stopPropagation();
        });

        // mail client button in index page
        $("a.mail-client-action-link").click(function(){
            var client = $(this).attr("data-default-webmail-app");
            SetNvData("default_webmail_app", client, handleSetNvData);
        });

        // navbar overlay
        $("#btnNavbarOverlayConfirm, #btnUserPref").click(function() {
            var tutorialContainer = $(".navbar-overlay-message:not(.hidden)");
            if( tutorialContainer.length ) {
                completeTutorial(tutorialContainer);
            }
        });
    });

})();