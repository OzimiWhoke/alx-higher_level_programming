<script>
  $(document).ready(function() {
    $.ajax({
      url: "https://fourtonfish.com/hellosalut/?lang=fr",
      success: function(data) {
        $('#hello').text(data.hello);
      },
      error: function() {
        $('#hello').text("Error fetching translation.");
      }
    });
  });
</script>
