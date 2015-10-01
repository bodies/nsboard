% include('header.tpl')
    <div id="login">
      <form class="form-inline" id="form-login" method="post" action="{{action}}">
        <div class="form-group form-group-sm">
          <lable for="inputId" class="sr-only">ID</lable>
          <input type="text" class="form-control" id="inputId" name="user_id" placeholder="ID" />
        </div>  <!-- id -->
        <div class="form-group form-group-sm">
          <label for="inputPassword" class="sr-only">Password</label>
          <input type="password" class="form-control" id="inputPassword" name="passwd" placeholder="Password" />
        </div> <!-- password -->
        <button type="submit" class="btn btn-sm btn-primary">로그인</button>
      </form>
    </div>  <!-- #login -->
% include('footer.tpl')