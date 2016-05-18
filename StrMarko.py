#!/home/students/2017/stiven.peter/public_html/proj/pyth/bin/python
print "Content-Type: text/html\n" 
print ""
import cgi
import random
import cgitb
cgitb.enable()
try :
    execfile("coll.py")
    def FStoD():
        '''
        Converts cgi.FieldStorage() return value into a standard dictionary
        '''
        d = {}
        formData = cgi.FieldStorage()
        for k in formData.keys():
            d[k] = formData[k].value
        return d    
    d = FStoD()
    ListStock = d.values()
    MegaList = DictMaker()

    def checker(compName) :
        if compName  in MegaList :
            thestock = MegaList[compName]
            return thestock
        else :
            thestock = compName
            return thestock

     
    execfile("alpha.py")


    def greatexcp(astock) :
        try :
            pullData(astock)
            processor(astock)
            ver = astock
        except :
            ver =  random.choice(MegaList.values())
        return ver

    def exceptionhandler() :
        ctr = 0
        while ctr < len(ListStock) :
            compTic = ListStock[ctr].strip(".!*)#%#")
            compTic = checker(compTic)
            finaltic = greatexcp(compTic)
            ListStock[ctr] = finaltic
            ctr += 1
    exceptionhandler()
    StockList = ListStock
    execfile("Markowitz.py")            
    htmlStr = "<!Doctype html>"
    htmlStr += """
    <html>
        
    <head>
      <title>W.P Financial</title>
     <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/css/bootstrap.min.css">
      <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
      <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.4/js/bootstrap.min.js"></script>
      <script src="jquery.js" type="text/javascript"></script>
      <script src="jquery.smart_autocomplete.js" type="text/javascript"></script>
      <script type="text/javascript">     
          $(function(){
            var stocks = """
    htmlStr += str(MegaList.keys())
    htmlStr += """
            $("#type_ahead_autocomplete_field").smartAutoComplete({source : stocks})
                          });
    </script>
        
    </head>
    <div id="wrap">

      <!-- Fixed navbar -->
      <div class="navbar navbar-inverse">
        <div class="container-fluid">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#" style="margin-top: 6px">W.P Financial</a>
          </div>
          <div class="collapse navbar-collapse">
            <ul class="nav navbar-nav" style="background-color: transparent">
              <li><a href="home.html">Home</a></li>
              <li><a href="markowitz.html">Portfolio Optimization</a></li>
              <li><a href="stock.html">Stock Search</a></li>
              <li><a href='industry.html'>Top Sharpe Finder</a></li>
              <li><a href="about.html">About</a></li>
            </ul> <!-- end navmenu -->
              <form action="wrapper.py" method="get" style="display: inline;" ><input type="text" autocomplete="off" id="type_ahead_autocomplete_field" name='comp' style="margin-top: 24px; float: right; height: 30px; border: 4px solid #d4d0ba; color: indianred" /> <input type="submit" style="margin-top: 24px; float: right; height: 30px; border-radius: 5px; border: 0;" /></form>
          </div><!--/.nav-collapse -->
        </div>
      </div>
        
    <style>
        
        body {
        background-color: lemonchiffon; 
        padding: 3px;
    }
        ul li {list-style: none; cursor: pointer;}
        li.smart_autocomplete_highlight {background-color: #C1CE84;}
        ul { margin: 10px 0; padding: 5px; background-color: #E3EBBC; }
        
        </style>    

    """   
    htmlStr += "<head><title>Portfolio Optimization</title></head></html>\n"
    htmlStr += "<head> <link rel='stylesheet' src='endStyle.css'> <script src='script.js'></script></head>"
    htmlStr += """
    <div class="container">
    <ul class="nav nav-pills nav-justified">
      <li ><a href="#Stocks" data-toggle="pill">Stocks</a></li>
      <li><a href="#Portfolio" data-toggle="pill">Portfolio Distribution</a></li>
     <li><a href="#Performance" data-toggle="pill">Portfolio Performance</a></li>

    </ul>
    <div class="tab-content">
    """
    htmlStr += " <div  class='tab-pane active' id='Stocks'><section role='tabpanel' aria-hidden='false' class='content active' id='panel2-1'> \
        <center><img src='stocks.png'></center>  \
      </section></div> \
    <div  class='tab-pane active' id='Portfolio'><section role='tabpanel' aria-hidden='false' class='content active' id='panel2-1'> \
        <center><img src='port.png'></center>  \
      </section></div> \
    <div  class='tab-pane active' id='Performance'><section role='tabpanel' aria-hidden='false' class='content active' id='panel2-1'> \
        <center><img src='dist.png'></center>  \
      </section></div> \
      </div></body></html> "
    print htmlStr
except :
    htmlStr = '<!Doctype html><html> \
    <meta HTTP-EQUIV="REFRESH" content="0; url=try.html"> \
    </html> ' 
    print htmlStr
