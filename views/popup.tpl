<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <script>alert("{{! msg }}");
    % if defined('dest'):
    window.location.href="{{ dest }}";
    % else:
    window.history.back();
    %end
    </script>
  </head>
  <body></body>
</html>