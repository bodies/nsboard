% include('header.tpl')
			<div class="story-view">
				<h3><a href="/b/{{ data['book_num'] }}">{{ data['book_title'] }}</a></h3>
				<h4>{{ data['title'] }}</h4>
				<p class="text">{{ !data['story'] }}</p>
				<p class="keywords">키워드 | {{ !', '.join(data['keywords']) }}</p>
				<div>
					<button class="btn btn-default btn-sm">
						<span class="glyphicon glyphicon-heart"></span>&nbsp;추천
					</button>
				</div>
				<div class="story-nav">
					<div class="btn-group">
						<a href="" class="btn btn-default btn-sm" role="button">
							<span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
						<a href="" class="btn btn-default btn-sm" role="button">
							<span class="glyphicon glyphicon-list"></span> 전체 보기</a>
						<a href="" class="btn btn-default btn-sm" role="button">
								다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
					</div>


					<div class="pull-left">
						<a href="" class="btn btn-default btn-sm">
							<span class="glyphicon glyphicon-chevron-left"></span> 이전 화</a>
					</div>
					<div class="pull-right">
						<a href="" class="btn btn-default btn-sm">
							다음 화 <span class="glyphicon glyphicon-chevron-right"></span></a>
					</div>
				</div>

			</div>  <!-- story-view -->
% include('footer.tpl')
