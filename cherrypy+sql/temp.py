<!DOCTYPE html>
<html>
  <head>
    <link href="/style.css" rel="stylesheet">
    <script src="http://code.jquery.com/jquery-2.0.3.min.js"></script>
    <script type="text/javascript">
      $(document).ready(function() {
        $("#generate-string").click(function(e) {
          $.post("/generator", {"length": $("input[name='length']").val()})
           .done(function(string) {
            $("#the-string").show();
            $("#the-string input").val(string);
          });
          e.preventDefault();
        });
        $("#replace-string").click(function(e) {
          $.ajax({
            type: "PUT",
            url: "/generator",
            data: {"another_string": $("#the-string input").val()}
          })
          .done(function() {
            alert("Replaced!");
          });
          e.preventDefault();
        });
        $("#delete-string").click(function(e) {
          $.ajax({
            type: "DELETE",
            url: "/generator"
          })
          .done(function() {
            $("#artist-name").hide();
			$("#song-name").hide();
          });
          e.preventDefault();
        });
      });
    </script>
  </head>
  <body>
    <div id="artist-name">
      <input type="text" />
      <button id="insert-artist">Insert artist</button>
    </div>
	<div id="song-name">
      <input type="text" />
      <button id="insert-title">Insert title</button>
    </div>
  </body>
</html>
