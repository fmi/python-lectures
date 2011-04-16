#!/usr/bin/perl
use strict;
use warnings;

use FileHandle;
use IPC::Open2;

sub produce {
    $_ = $_[0];
    s/\n\r/\n/g;
    s/\r/\n/g;
    my @slides = split /^\s*(?===\s+.*?\s+==\w*$)/m;
    print opening_slide(shift @slides)."\n\n";
    print format_slide($_)."\n\n" for (@slides);
    print closing_slide();
}

sub opening_slide {
    $_ = shift;
    my ($title, $date, $intro) = (/^(.*?)\n(.*?)\n(.*)$/s);

    $intro = html_escape(trim($intro));
    $intro =~ s#\n#<br />\n#g;
    $intro =~ s#  # &nbsp;#g;

    html_head($title, $date, $intro);
}

sub format_slide {
    $_ = shift;
    s/\{\{\{(\w+)?\n(.*?)\n\}\}\}/'{{{'.codenote($2, $1).'}}}'/smge;
    s/"(.+?)"/&#8222;$1&#8220;/g;
    s#^==\s+(.*?)\s+==(l+)?(.*)\z#'<div class="slide'.($2 ? " ".("long" x length($2)) : "")."\">\n  <h1>$1</h1>$3\n</div>"#se;
    s#\*\*\*(.*?)\*\*\*#<strong>$1</strong>#g;
    s#`(.*?)`#<code>$1</code>#sg;
    s#\[\[(.+?) (\S+?:\S+?)\]\]#<a href="$2">$1</a>#g;
    s#(?<!")(http://\S+)#<a href="$1">$1</a>#g;
    s#((^ \*.*?\n)+)#  <ul>\n$1  </ul>\n#mg;
    s#((^ \#.*?\n)+)#  <ol>\n$1  </ol>\n#mg;
    s/^ [\#*]\s*(.*)$/    <li>$1<\/li>/mg;
    s#<li>\(\((.*?)\)\)</li>#<li class="incremental">$1</li>#g;
    s#((^[^ <{\n].+?\n)+)#'  <p>'.trim($1)."</p>\n"#mge;
    s#<p>\(\((.*?)\)\)</p>#<p class="incremental">$1</p>#mg;
    s/\n+/\n/g;
    s/--/&mdash;/g;
    s/\.\.\./&hellip;/g;
    s/\{\{\{(\d+)\}\}\}/format_codenote($1)/ge;
    $_;
}

# === CODE NOTES ==========================================================
our @codenotes;

sub codenote {
    push @codenotes, {code => $_[0], format => $_[1]};
    $#codenotes;
}

sub format_codenote {
    my ($note, $formats) = $codenotes[shift];
    $formats = {
        bare => sub { $_[0] },
        code => sub { "  <pre><code>".html_escape($_[0])."</code></pre>" },
        python => sub { "  <pre class=\"prettyprint\">\n$_[0]\n</pre>" },
        with_output => sub { join "\n", $formats->{python}->($_[0]), $formats->{code}->(python_output($_[0])) },
    };
    no warnings;
    ($formats->{$note->{format}} || $formats->{python})->($note->{code});
}

sub python_output {
    my ($code, $result) = (shift);
    open2(*Reader, *Writer, "python3.0");
    print Writer $code."\n";
    close Writer;
    $result .= $_ while (<Reader>);
    close Reader;
    chomp $result;
    $result;
}

# === TEXT UTILS ======================================================================
sub trim {
    $_ = shift;
    s/^\s+//;
    s/\s+$//;
    $_;
}

sub html_escape {
    $_ = shift;
    s/&/&amp;/g;
    s/>/&gt;/g;
    s/</&lt;/g;
    $_;
}


sub html_head {
    my ($title, $date, $intro) = @_;
    <<"HEAD"
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">

<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Програмиране с Python: $title</title>
<!-- metadata -->
<meta name="generator" content="S5" />
<meta name="version" content="S5 1.1" />
<meta name="presdate" content="16.04.2008" />
<meta name="author" content="Стефан Кънев, Николай Бачийски, Точо Точев и Димитър Димитров" />
<!-- configuration parameters -->
<meta name="defaultView" content="slideshow" />
<meta name="controlVis" content="hidden" />
<!-- style sheet links -->
<link rel="stylesheet" href="ui/python/slides.css" type="text/css" media="projection" id="slideProj" />
<link rel="stylesheet" href="ui/python/outline.css" type="text/css" media="screen" id="outlineStyle" />
<link rel="stylesheet" href="ui/python/prettify.css" type="text/css" media="screen" id="prettyifyStyle" />
<link rel="stylesheet" href="ui/python/print.css" type="text/css" media="print" id="slidePrint" />
<link rel="stylesheet" href="ui/python/opera.css" type="text/css" media="projection" id="operaFix" />
<!-- S5 JS -->
<script src="ui/python/slides.js" type="text/javascript"></script>
<script src="ui/python/prettify.js" type="text/javascript"></script>
</head>
<body>

<div class="layout">
<div id="controls"><!-- DO NOT EDIT --></div>
<div id="currentSlide"><!-- DO NOT EDIT --></div>
<div id="header"></div>
<div id="footer">
<h1>&bdquo;$title&ldquo;, част от курса <a href="http://fmi.py-bg.net/">Програмиране с Python</a></h1>
<h1>Текстът на тази презентация се разпространява под <a href="http://creativecommons.org/licenses/by/3.0/deed.bg">Creative Commons Attribution</a></h1>
</div>

</div>


<div class="presentation">

<div class="slide">
<h1>$title</h1>
<h3>&bdquo; Програмиране с Python&ldquo;, <acronym title="Факултет по Математика и Информатика при Софийски Университет">ФМИ</acronym></h3>
<h4>$intro</h4>
<h4>$date</h4>
</div>
HEAD
;
}

sub closing_slide {
    <<TAIL
</div>
<script type="text/javascript" language="JavaScript">prettyPrint()</script>
</body>
</html>
TAIL
;
}


produce join "", <>;
