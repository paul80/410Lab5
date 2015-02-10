<!doctype html>
<title> CMPUT410 - Jinja Lab</title>
<link rel=stylesheet type=text/css href="{{ url_for('static', filename='style.css') }}">
<div class= "page">
    <h1>TODO-List</h1>
    <div class="metanav">
    {% if not session.logged_in %}
        <a href="{{ url_for('login')}}">Log in</a>
    {% else %}
        <a href= "{{ url_for('logout') }}">Log out</a>
    {% endif %}
    </div>
    {% for message in get_flashed_messages() %}
    <div class="flash"> {{message}} </div>
    {%endfor%}
    {% block body%} {%endblock%}

</div>