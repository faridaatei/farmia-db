{% extends 'layouts.html'%}
{% block content%}
<form class="" action="{{url_for('generate')}}" method="post">
<div class="form-group">
  <label for="title">animals</label>
  <input type="text" name="animal" class="form-control" placeholder="type of animal" value="">
</div>
<div class="form-group">
  <label for="body">type of feed</label>
  <input type="text" name="type of feed" class="form-control" placeholder="type of feed" value="">
</div>

</div> -->
<button type="submit" name="button">Generate</button>
</form>
{%endblock%}