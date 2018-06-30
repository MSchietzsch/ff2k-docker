tinymce.init({
    selector: '#chapter_text',
    height: 500,
    menubar: false,
    branding: false,
    plugins: [
      'advlist autolink lists link image charmap print preview anchor textcolor',
      'searchreplace visualblocks code fullscreen',
      'insertdatetime media table contextmenu paste code help wordcount', 'autosave'
    ],
    toolbar: 'formatselect | bold italic backcolor  | alignleft aligncenter alignright alignjustify | undo redo | bullist numlist outdent indent | removeformat | help | restoredraft',
    content_css: [
      '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
      '//www.tinymce.com/css/codepen.min.css']
  });