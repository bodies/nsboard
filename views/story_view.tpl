% include('header.tpl')
			<div class="story-view">
				<h2><a href="/b/{{ data['book_num'] }}">{{ data['book_title'] }}</a></h2>
				<div class="story-nav clearfix">
					<div class="pull-left">
						<a href="" class="btn btn-link">
							<span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
					</div>
					<div class="pull-right">
						<a href="" class="btn btn-link">
							다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
					</div>
				</div>

				<h3>{{ data['title'] }}</h3>
				<p class="text">{{ !data['story'] }}</p>
				<p class="keywords"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;
				% for kw in data['keywords']:
					<button type="button" class="btn btn-default btn-sm">{{ kw }}</button>
				% end
				<!-- % for kw in data['keywords']: -->
					<!-- <a href="/t/{{ kw }}"><span class="label label-default">{{ kw }}</span></a> -->
				<!-- % end -->
				<!-- {{ !', '.join(data['keywords']) }} -->
				</p>
				<div class="buttons">
					<a href="/b/{{ data['book_num'] }}" class="btn btn-primary" role="button">
						<span class="glyphicon glyphicon-list"></span>&nbsp;목차 보기
					</a>
					&nbsp;
					<button class="btn btn-warning">
						<span class="glyphicon glyphicon-heart"></span>&nbsp;추천
					</button>
				</div>
				<div class="story-nav clearfix">
					<div class="pull-left">
						<a href="" class="btn btn-link">
							<span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
					</div>
					<div class="pull-right">
						<a href="" class="btn btn-link">
							다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
					</div>
				</div>
			</div>  <!-- story-view -->
% include('footer.tpl')
