// Navigates to a specific tab when page loads based on the hash
// The hash does not match the exact id to prevent scrolling
$(document).ready(() => {
    let selectedTab = window.location.hash;
    if (selectedTab !== "") {
        $(`#${selectedTab.substring(1)}-tab`).tab('show');
    }
})
