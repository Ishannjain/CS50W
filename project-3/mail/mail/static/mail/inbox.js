document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between view
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);
  document.querySelector('#compose-form').addEventListener('submit', send_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#emails-detail-view').style.display = 'none';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';

}
function view_email(id){
  fetch(`/emails/${id}`)
.then(response => response.json())
.then(emails => {
    // Print email
    console.log(emails);
    document.querySelector('#emails-view').style.display = 'none';
    document.querySelector('#compose-view').style.display = 'none';
    document.querySelector('#emails-detail-view').style.display = 'block';
    document.querySelector('#emails-detail-view').innerHTML =`
    <ul class="list-group">
  <li class="list-group-item"><Strong>From:</strong>${emails.sender}</li>
  <li class="list-group-item"><Strong>To:</strong>${emails.recipients}</li>
  <li class="list-group-item"><Strong>Subject:</strong>${emails.subject}</li>
  <li class="list-group-item"><Strong>Timestamp:</strong>${emails.timestamp}</li>
  <li class="list-group-item"><Strong>Body:</strong>${emails.body}</li>
  </ul>`
    if(!emails.read){
      fetch(`/emails/${emails.id}`, {
        method: 'PUT',
        body: JSON.stringify({
            read: true
        })
      })
    }
    // archive/unarchive
      const element = document.createElement('button');
      element.innerHTML = emails.archived? 'Unarchive':'Archive';
      element.className= emails.archived?'btn btn-danger':'btn btn-success';
      element.addEventListener('click', function() {
       
          fetch(`/emails/${emails.id}`, {
            method: 'PUT',
            body: JSON.stringify({
              archived:!emails.archived
            })
          })
        .then(()=>{
          load_mailbox('archive')
        })
      });
      document.querySelector('#emails-detail-view').append(element);

      //reply button
      const reply = document.createElement('button');
      reply.innerHTML ="Reply";
      reply.className="btn btn-info";
      reply.addEventListener('click',function(){
      compose_email();
      document.querySelector('#compose-recipients').value =emails.sender;
      let subject=emails.subject();
      if(subject.split('',1)[0]!="Re:"){
        subject="Re:"+emails.subject;
      }
      document.querySelector('#compose-subject').value =subject;
      
      document.querySelector('#compose-body').value = `On${emails.timestamp} ${emails.sender} wrote: ${emails.body}`;
    
      });
      document.querySelector('#emails-detail-view').append(reply);
});
}
function load_mailbox(mailbox) {
  
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#emails-detail-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
      // Print emails
      emails.forEach(singleEmail =>{
        console.log(singleEmail);

      const newEmail = document.createElement('div');
      newEmail.className="list-group-item";
      newEmail.innerHTML = `
      <h5>Sender:${singleEmail.sender}</h5>
      <h4>Subject:${singleEmail.subject}</h4>
      <p>TimeStamp:${singleEmail.timestamp}</p>
      `;
      newEmail.className=singleEmail.read?'read':'unread';
      newEmail.addEventListener('click', function() {
          view_email(singleEmail.id);
      });
      document.querySelector('#emails-view').append(newEmail);
  });
});
}
function send_email(event){
  event.stopImmediatePropagation();
  const recipients=document.querySelector('#compose-recipients').value;
  const subject=document.querySelector('#compose-subject').value;
  const body=document.querySelector('#compose-body').value;

    fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
        recipients:recipients,
        subject:subject,
        body:body
    })
    })
    .then(response => response.json())
    .then(result => {
      // Print result
      console.log(result);
      load_mailbox('sent');
    });
}
