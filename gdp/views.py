import os
from django.template.loader import get_template
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import Context, RequestContext
from django.shortcuts import redirect
from  Global_Deisgn_post.gdp.forms import RegistrationForm
def home(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    #return render_to_response('index.html',variables )
    zip_folder(r'//home//gdp//Global_Deisgn_post',r'//home//gdp//Global_Deisgn_post.zip')
    return HttpResponse(os.path.dirname('/home/gdp/Global_Deisgn_post'))

def favorites(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('favourite.html',variables )

def bazaar(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('bazar.html',variables )

def mygdp(request):
    form =RegistrationForm()
    variables = RequestContext(request, {'page_message':'The request was unable to send due to some technical issues.','error_header':'Error!'})
    return render_to_response('mygdp.html',variables )

def test(request):
    k=request.user.id
    import os
    import zipfile
    import sys
    zip_folder(r'//home//gdp//Global_Deisgn_post',r'//home//gdp//Global_Deisgn_post.zip')
    #tabs.zip
    #zip = zipfile.ZipFile(r'/home/tomjoy/plikes/static/images/userimages/tabs.zip')
    #zip.extractall(r'/home/tomjoy/plikes/static/gallery/tom')
    #file=open('/home/tomjoy/plikes/static/plikes.zip','rb')
    #pdfData=file.read()
    #file.close()
    #response= HttpResponse(pdfData,mimetype="application/submimetype")
    #response['Content-Disposition'] = 'attachment; filename=' + str('Plikes.zip')
    #return response
    template = get_template('test.html')
    variables = RequestContext(request,{'People':'g'})
    output = template.render(variables)
    return HttpResponse(output)

def zip_folder(folder_path, output_path):
    """Zip the contents of an entire folder (with that folder included
    in the archive). Empty subfolders will be included in the archive
    as well.
    """
    import zipfile
    import sys
    import os
    parent_folder = os.path.dirname(folder_path)
    # Retrieve the paths of the folder contents.
    contents = os.walk(folder_path)
    try:
        zip_file = zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED)
        for root, folders, files in contents:
            # Include all subfolders, including empty ones.
            for folder_name in folders:
                absolute_path = os.path.join(root, folder_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print "Adding '%s' to archive." % absolute_path
                zip_file.write(absolute_path, relative_path)
            for file_name in files:
                absolute_path = os.path.join(root, file_name)
                relative_path = absolute_path.replace(parent_folder + '\\',
                                                      '')
                print "Adding '%s' to archive." % absolute_path
                zip_file.write(absolute_path, relative_path)
        print "'%s' created successfully." % output_path
    except IOError, message:
        print message
        sys.exit(1)
    except OSError, message:
        print message
        sys.exit(1)
    except zipfile.BadZipfile, message:
        print message
        sys.exit(1)
    finally:
        zip_file.close()

def unzip(request,filename):
    import zipfile
    #zipFileName='/home/tomjoy/plikes/static/gallery/'+str(fName)
    try:
        zip = zipfile.ZipFile('/static/js//static/js/static/'+str(filename)+'.zip')
        zip.extractall('/home/gdp/Global_Deisgn_post/static/')

    except Exception,e:
        return HttpResponse(e)

    return HttpResponse("Successfully extracted")