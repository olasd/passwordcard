<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>{{title or "PasswordCard"}}</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="A wallet-card sized password card">
    <meta name="author" content="Nicolas Dandrimont">

    <!-- Le styles -->
    <link href="/static/css/bootstrap.min.css" rel="stylesheet">
    <style>
      body {
        padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
      }


      .footer {
        padding: 70px 0;
        margin-top: 70px;
        border-top: 1px solid #e5e5e5;
        background-color: #f5f5f5;
      }
      .footer p {
        margin-bottom: 0;
        color: #777;
      }
    </style>
    <link href="/static/css/bootstrap-responsive.min.css" rel="stylesheet">

    <!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
  </head>

  <body>

    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </a>
          <a class="brand" href="#">PasswordCard++</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              <li class="active"><a href="/">Home</a></li>
            </ul>
            <ul class="nav pull-right">
              <li><a href="https://github.com/olasd/passwordcard" target="_blank">Source</a></li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>

    <div class="container">
    %include
    </div> <!-- /container -->

    <footer class="footer">
      <div class="container">
        <p class="muted credit">By <a href="http://twitter.com/olasd" target="_blank">Nicolas Dandrimont</a> and contributors. Released under the <a href="http://www.gnu.org/licenses/agpl-3.0.html" target="_blank">GNU AGPL</a> v3 or later. Original idea and algorithm from <a href="http://passwordcard.org/" target="_blank">pepsoft.org</a>.</p>
      </div>
    </footer>
    <!-- Le javascript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="/static/js/jquery-1.8.2.min.js"></script>
    <script src="/static/js/bootstrap.min.js"></script>

  </body>
</html>
