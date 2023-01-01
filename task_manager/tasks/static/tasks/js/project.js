function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function project_put_status(project_id, state){
    fetch(`/project/${project_id}/status/put`, {
      method: 'PUT',
      body: JSON.stringify({status: state}),
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    })
}

function project_put_priority(project_id, state){
    fetch(`/project/${project_id}/priority/put`, {
      method: 'PUT',
      body: JSON.stringify({priority: state}),
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    })
}

function task_put_status(task_id, state){
    fetch(`/task/${task_id}/status/put`, {
      method: 'PUT',
      body: JSON.stringify({status: state}),
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    })
}

function task_put_status(task_id, member){
    fetch(`/task/${task_id}/assignment/put`, {
      method: 'PUT',
      body: JSON.stringify({assignment: member}),
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    })
}

function handleChange(project_id, user) {
     fetch(`/project/${project_id}/member/put`, {
      method: 'PUT',
      body: JSON.stringify({member: user}),
      headers: { "X-CSRFToken": getCookie('csrftoken') }
    })
}
