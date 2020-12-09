function delete_client(id) {
    console.log("id: " + id)
    window.location.assign('/delete-client-and-contact-information?id=' + id)
}