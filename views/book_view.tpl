% include('header.tpl')
			<div class="page-view-book">
				<h3>{{ info['title'] }}</h3>
				% if not info:
				<p>작품 정보가 존재하지 않습니다.</p>
				% else:
        <div>
          <p class="book-intro">{{ info['intro'] if info['intro'] else '...' }}</p>
          <p class="keywords"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;
            % for kw in info['keywords']:
            <a href="/k/{{ kw }}"><span class="label label-default">{{ kw }}</span></a>
            % end
          </p>
        </div>
        <div class="buttons">
          <a href="/b/{{ info['num'] }}/1" class="btn btn-success btn-sm" role="button">
            <span class="glyphicon glyphicon-align-justify" aria-hidden="true"></span>&nbsp;첫 화 보기
          </a>
          <a href="" class="btn btn-primary btn-sm" role="button">
            <span class="glyphicon glyphicon-bookmark" aria-hidden="true"></span>&nbsp;즐겨찾기
          </a>
        </div>
        % if not list:
        <p>등록된 글이 없습니다.</p>
        % else:
        <div class="story-list">
          <div class="story-list-header clearfix">
            <div class="pull-left">총 {{ info['story_count'] }} 편</div>
            <div class="pull-right">
            최근 등록일: <span title="{{ info['update_date'] }}">{{ info['update_date'].strftime('%Y/%m/%d') }}</span>
            </div>
          </div>

          % for r in list:
          <div class="story-list-item clearfix">
            <div class="pull-left">
              <a href="/s/{{ r['num'] }}">{{ r['title'] }}</a>
            </div>
            <div class="pull-right">
              <span title="{{ r['mod_date'] }}">{{ r['mod_date'].strftime('%Y/%m/%d') }}</span>
            </div>
          </div>  <!-- story-list-item -->
          % end
        </div>  <!-- story-list -->
        % end
        % end
			</div>
% include('footer.tpl')
