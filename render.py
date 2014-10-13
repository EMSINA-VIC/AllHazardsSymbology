import os
import subprocess

output_folder = os.path.dirname(os.path.realpath(__file__)) + "\\render"
set_name = ""
print "outputting to: " + output_folder

for root, dirs, files in os.walk("C:\code\git\AllHazardsSymbology\source"):
    print 'found ' +  ' '.join(files)

    #for dir in dirs:


    for name in files:
        print "root " + root
        print "new file " + ' '.join(root) + " | " + ''.join(dirs) + " | " + name
        if name.endswith((".svg", ".png")):
                set_name = os.path.basename(root)
                print "**Found svg: " + name + " for set " + set_name


                #set_output_folder = output_folder + '\\' + set_name + '\\'

                #if not os.path.exists(set_output_folder):
                #    os.makedirs(set_output_folder)

                orig_name = name
                #generate  the call to inkscape.
                # eg inkscape.exe --export-png "test.png" "test.svg"
                #'"C:\\Program Files\\Inkscape\\inkscape.exe"',

                #png versions
                set_output_folder = output_folder + '\\png\\' + set_name + '\\'
                if not os.path.exists(set_output_folder):
                    os.makedirs(set_output_folder)

                args = ['inkscape.exe',
                        '-z',
                        '--export-png',
                        '"' + set_output_folder + name.replace(".svg",".png")    + '"',
                        '"' + root + '\\' + orig_name + '"']
                print "Executing inkscape with :" + ' '.join(args)
                os.system(' '.join(args))
                #subprocess.call(args)


                set_output_folder = output_folder + '\\emf\\' + set_name + '\\'

                if not os.path.exists(set_output_folder):
                    os.makedirs(set_output_folder)

                name = orig_name
                args = ['inkscape.exe',
                        '-z',
                        '--export-emf',
                        '"' + set_output_folder + name.replace(".svg",".emf")    + '"',
                        '"' + root + '\\' + orig_name + '"']
                print "Executing inkscape with :" + ' '.join(args)
                os.system(' '.join(args))


                args = ['inkscape.exe',
                        '-z',
                        '--export-bmp',
                        '"' + set_output_folder + name.replace(".svg",".bmp")    + '"',
                        '"' + root + '\\' + orig_name + '"']
                #print "Executing inkscape with :" + ' '.join(args)
