% include('admin_header.tpl')
			<div>
				<div class="panel panel-default">
					<div class="panel-heading">
						<h4 class="panel-title">
						% if defined('mod'):
							{{ data['book_title'] }} - 제 {{ data['queue_num'] }}화 고치기
						% else:
							{{ data['book_title'] }} - 제 {{ data['story_count'] + 1 }}화
						% end
						</h4>
					</div>	<!-- panel-heading -->
					<div class="panel-body">
						<form id="form-new-story" method="post" action="{{ action }}">
							<div class="form-group form-group-sm">
								<label for="inputQueue" class="sr-only">연재 회차</label>
								<input type="text" id="inputQueue" class="form-control" name="queue" placeholder="연재 회차" value="{{ data['queue_num'] }}"/>
							</div>
							<div class="form-group form-group-sm">
								<label for="inputStoryTitle" class="sr-only">제목</label>
								<input type="text" id="inputStoryTitle" class="form-control" name="title" placeholder="제목" value="{{ data['title'] }}" />
							</div>
							<div class="form-group form-group-sm">
								<label for="textareaStory" class="sr-only">본문</label>
								<textarea class="form-control" id="textareaStory" rows="24" name="story" placeholder="본문">{{ data['story'] if defined('mod') else '' }}</textarea>
							</div>
							<div class="form-group form-group-sm">
							% if defined('mod') and data['public']:
								% radio_p = 'checked'
								% radio_np = ''
							% else:
								% radio_p = ''
								% radio_np = 'checked'
							% end
	              <label class="radio-inline">
	                <input type="radio" name="is_public" value="True" {{ radio_p }}>공개
	              </label>
	              <label class="radio-inline">
	                <input type="radio" name="is_public" value="False" {{ radio_np }}>비공개
	              </label>
	            </div>
	            <div class="form-group form-group-sm">
	            	<div class="pull-left">
		            	<a href="/a/b/{{ data['num'] }}/list" class="btn btn-sm btn-default" role="button">돌아가기</a>
		            </div>
		            <div class="pull-right">
									<button type="submit" class="btn btn-sm btn-primary">저장</button>
								</div>
							</div>
						</form>
					</div>	<!-- panel-body -->
				</div>	<!-- panel -->
			</div>  <!-- col-md-10 -->
% include('footer.tpl')
