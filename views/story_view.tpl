% include('header.tpl')
			<div>
				<h3><a href="/b/{{ data['book_num'] }}">{{ data['book_title'] }}</a></h3>
				<h4>{{ data['title'] }}</h4>
				<table class="table table-condensed">
					<tr>
						<td>작성일</td>
						<td>{{ data['pub_date'] }}</td>
						<td>수정일</td>
						<td>{{ data['mod_date'] }}</td>
						<td>조회수</td>
						<td>{{ data['view_count'] }}</td>
						<td>추천수</td>
						<td>{{ data['like_count'] }}</td>
					</tr>
					<tr>
						<td>키워드</td>
						<td colspan="7">{{ !', '.join(data['keywords']) }}</td>
					</tr>
				</table>
				<p class="text">{{ !data['story'] }}</p>
			</div>
% include('footer.tpl')
