% include('header.tpl')
% prev_dp = ' hidden' if not data['prev'] else ''
% next_dp = ' hidden' if not data['next'] else ''
      <script src="/static/cookie.js"></script>
      <script src="/static/reader.js"></script>
      <div class="page-view-story">
        <h2><a href="/b/{{ data['book_num'] }}">{{ data['book_title'] }}</a></h2>
        <div class="story-nav clearfix">
          <div class="pull-left">
            <a href="/s/{{ data['prev'] }}" class="btn btn-link{{ prev_dp }}">
              <span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
          </div>
          <div class="pull-right">
            <a href="/s/{{ data['next'] }}" class="btn btn-link{{ next_dp }}">
              다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
          </div>
        </div>

        <h3>{{ data['title'] }}</h3>
        <div class="resizer clearfix">
          <button type="button" class="btn btn-sm btn-default pull-right" id="change-font-size" role="button">
            <span class="glyphicon glyphicon-plus"></span>
          </button>
          <!--<div class="btn-group pull-right btn-group-sm" role="group">-->
            <!--<button type="button" class="btn btn-default" aria-label="글자 축소" onclick="text_size_down();">-->
              <!--<span class="glyphicon glyphicon-minus"></span>-->
            <!--</button>-->
            <!--<button type="button" class="btn btn-default" aria-label="글자 확대" onclick="text_size_up();">-->
              <!--<span class="glyphicon glyphicon-plus"></span>-->
            <!--</button>-->
          <!--</div>-->
        </div>
        <div class="text">{{ !data['story'] }}</div>
        <p class="keywords"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;
        % for kw in data['keywords']:
          <!-- <a href="/k/{{ kw }}" class="btn btn-default btn-sm" role="button">{{ kw }}</a> -->
        <!-- % end -->
          <a href="/k/{{ kw }}"><span class="label label-default">{{ kw }}</span></a>
        % end
        <!-- {{ !', '.join(data['keywords']) }} -->
        </p>
        <div class="buttons">
          <a href="/b/{{ data['book_num'] }}" class="btn btn-primary" role="button">
            <span class="glyphicon glyphicon-list"></span>&nbsp;목차
          </a>
          &nbsp;
          <button class="btn btn-warning">
            <span class="glyphicon glyphicon-heart"></span>&nbsp;추천
          </button>
        </div>
        <div class="story-nav clearfix">
          <div class="pull-left">
            <a href="/s/{{ data['prev'] }}" class="btn btn-link{{ prev_dp }}">
              <span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
          </div>
          <div class="pull-right">
            <a href="/s/{{ data['next'] }}" class="btn btn-link{{ next_dp }}">
              다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
          </div>
        </div>
      </div>  <!-- page-view-story -->
% include('footer.tpl')
