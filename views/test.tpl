% include('header.tpl')
<script src="/static/test.js"></script>
<div>
  <div class="btn-group btn-group-sm" role="group">
    <button type="button" class="btn btn-default" id="font_size_up">
      <span class="glyphicon glyphicon-plus"></span>
    </button>
    <button type="button" class="btn btn-default" id="font_size_down">
      <span class="glyphicon glyphicon-minus"></span>
    </button>
  </div>
</div>

<div>
  <button type="button" class="btn btn-default" id="change-font-size">
    <span class="glyphicon glyphicon-plus"></span>
  </button>
</div>


<div>
  <button type="button" class="btn btn-default" id="like_button" data-story-number="111">
    추천
  </button>
</div>


<input type="button" id="bbb" value="GET!" />
  <div class="text">
    <p>당신은 누구십니까? 남자는 그렇게 물었다</p>
  </div>

% include('footer.tpl')
