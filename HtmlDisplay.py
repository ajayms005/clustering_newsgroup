#created by Ajay M S

import webbrowser
import os
import codecs
def displayMainPage(newsClusters):

    currentDir= os.path.dirname(os.path.realpath(__file__))+"\cluster"
    MainClusterDisplay='MainClusterDisplay.html'
    ClusterContent="<html>\n<head><h1 align=\"middle\"> CLUSTERS WILL BE DISPLAYED HERE </h1>\n</head>\n</html>"
    f = open(MainClusterDisplay,'w')
    f.write(ClusterContent)
    f.close()    
    
    scriptForm=["<html>\n<head><h1 align=\"center\">WELCOME TO IR PROJECT</h1></head>\n<body>\n<script type=\"text/javascript\">\n function goToPage763(mySelect){ \n PageIndex2=mySelect.selectedIndex;\nif(mySelect.options[PageIndex2].value != \"none\"){\n"]
    scriptForm.append("frames['iframe2'].location.href = mySelect.options[PageIndex2].value;\n}\n}\n</script>\n")
    
    clusterForm=["<form name=\"form763\">\n<p>\n"]
    clusterForm.append("<select name=\"select763\" size=\"1\" onchange=\"goToPage763(this.form.select763)\">\n")
    clusterForm.append("<option value=\"none\" selected=\"selected\">Select a cluster </option>\n")
    
    for i in range(0,len(newsClusters)):
        cURL="<option value=\""+currentDir+str(i+1)+".html\">"+"CLUSTER "+str(i+1)+" LINK </option>\n"
        clusterForm.append(cURL)
    
    clusterForm.append("</select>\n</p>\n<p>\n")
    clusterForm.append("<div style=\"width:50%; float:left\">\n<iframe name=\"iframe2\" src=\""+currentDir+"\MainClusterDisplay.html" +"\" align=\"top\" width=\"100%\" height=\"1000\" align=\"middle\">If you can see this, your browser does not support iframes!</iframe>\n</div>\n")
    clusterForm.append("<div style=\"width:50%; float:left\">\n<iframe name=\"iframe3\" src=\""+currentDir+"\MainClusterDisplay.html" +"\" align=\"top\" width=\"100%\" height=\"1000\" align=\"middle\">If you can see this, your browser does not support iframes!</iframe>\n</div>\n")
    clusterForm.append("</p>\n</form>\n</body>\n</html>")
    scriptForm.extend(clusterForm)
    scriptForm=''.join(scriptForm)
    f = open('IRPROJECT.html','w')
    f.write(scriptForm)
    f.close()
    
    for i in range(0,len(newsClusters)):
        htmlContent=["<html>\n<head>\n<h1 align= center>CLUSTER "+str(i)+" CONTENTS </h1>\n</head>\n<body>\n"]
        clusContent=newsClusters[i]
        for k in range(0,len(clusContent)):
            htmlContent.append( "\n")
            link="<h4><a href=\""+clusContent[k].getUrl()+"\" target=\"iframe3\">"+clusContent[k].getTitle()+"</a></h4>"
            htmlContent.append(link)
        
        htmlContent.append("\n</body>\n</html>\n")
        htmlContent=''.join(htmlContent)
        cfilename='cluster'+str(i+1)+'.html'
        f = codecs.open(cfilename,'w',encoding='utf-8')
        f.write(htmlContent)
        f.close()
    filename = 'IRPROJECT.html'
    webbrowser.open_new_tab(filename)
