% include('admin_header.tpl')
    <div>
      <div class="panel panel-default">
        <div class="panel-heading">
          <h4 class="panel-title">
            % if defined('mod'):
              '{{ data['title']}}' 정보 수정
            % else:
              새 작품 등록
            % end
            % if defined('data') and data['series']:
              % radio_s = 'checked'
              % radio_ns = ''
            % else:
              % radio_s = ''
              % radio_ns = 'checked'
            % end
            % if defined('data') and data['public']:
              % radio_p = 'checked'
              % radio_np = ''
            % else:
              % radio_p = ''
              % radio_np = 'checked'
            % end
            % if defined('data') and data['complete']:
              % print(data['complete'])
              % radio_c = 'checked'
              % radio_nc = ''
            % else:
              % radio_c = ''
              % radio_nc = 'checked'
            % end

          </h4>
        </div>
        <div class="panel-body">
          <form id="form-new-book" method="post" action="{{ action }}">

            <div class="form-group form-group-sm">
              <label class="radio-inline">
                <input type="radio" name="is_series" value="True" {{ radio_s }}>장편
              </label>
              <label class="radio-inline">
                <input type="radio" name="is_series" value="False" {{ radio_ns }}>단편
              </label>
            </div>

            <div class="form-group form-group-sm">
              <label for="inputBookname" class="sr-only">작품 제목</label>
              <input type="text" class="form-control" id="inputBookname" name="title" placeholder="작품 제목" value="{{ data['title'] if defined('mod') else '' }}" >
            </div>

            <div class="form-group form-group-sm">
              <label for="inputKeywords" class="sr-only">키워드</label>
              <input type="text" class="form-control" id="inputKeywords" name="keywords" placeholder="키워드 (쉼표로 구분)" value="{{ ', '.join(data['keywords']) if defined('mod') else '' }}">
            </div>

            <div class="form-group form-group-sm">
              <label for="textareaBookintro" class="sr-only">작품 소개</label>
              <textarea class="form-control" rows="5" name="intro" placeholder="작품 소개">{{ data['intro'] if defined('mod') else '' }}</textarea>
            </div>

            <div class="form-group form-group-sm">
              <label class="radio-inline">
                <input type="radio" name="is_public" value="True" {{ radio_p }}>공개
              </label>
              <label class="radio-inline">
                <input type="radio" name="is_public" value="False" {{ radio_np }}>비공개
              </label>
            </div>
            % if defined('mod'):
            <div class="form-group form-group-sm">
              <label class="radio-inline">
                <input type="radio" name="is_complete" value="True" {{ radio_c }}>완결
              </label>
              <label class="radio-inline">
                <input type="radio" name="is_complete" value="False" {{ radio_nc }}>미완결
              </label>
            </div>
            % end

            <div class="form-group form-group-sm">
              <button type="submit" class="btn btn-sm btn-primary join-btn">작품 등록</button>
            </div>
            <div class="clearfix"></div>
          </form>
        </div>  <!-- panel-body -->
      </div>  <!-- panel -->
    </div>
% include('footer.tpl')
