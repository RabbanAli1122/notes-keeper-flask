function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    //   body is the data which is sent
    }).then((_res) => { // res finds if  there was an error in execution
      window.location.href = "/";
    });
  }