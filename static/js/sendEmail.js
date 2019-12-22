function sendMail(contact_form) {
    emailjs.send("gmail", "milestone_4_project", {
        "message": contact_form.message.value,
        "from_name": contact_form.full_name.value,
        "from_email": contact_form.emailaddress.value,
        "nature_of_enquiry": contact_form.nature_of_enquiry.value,
    })
        .then(
            function (response) {
                console.log("SUCCESS", response);
                setTimeout($("#modalMessage").modal(), 500); // the user will know that their message was sent successfully and is given feedback.
                document.getElementById("contact_form").reset() // the form is reset after submit button is hit
            },
            function (error) {
                console.log("FAILED", error);
            }
        );
    return false; // To block from loading a new page...
}


