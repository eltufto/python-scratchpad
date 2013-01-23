import os

def print_label(result_dir, info):
    print_dir = result_dir
    printer_name = 'LabelWriter-450'

    with open(os.path.join(print_dir, 'print.txt'), 'w') as print_job:
        for key in info:
            print_job.write('%s: %s\n' % (key, info[key]))

    print "Label is printing ..."
    cmd = ('lp -d %s -o landscape -o PageSize=w79h252.2 -o number-up=2 %s' %
    #cmd = ('lp -d %s -o landscape -o fit-to-page -o media=Custom.18x36 -o number-up=2 %s' %
    #cmd = ('lp -d %s -o landscape -o number-up=2 %s' %
            (printer_name, os.path.join(print_dir, 'print.txt')))
    os.system(cmd)


info = {
  'Work Order': 'WOtest',
  'Product ID': 'PIDtest',
  'Revision': 'RV#Test'
}
print_label('/home/stephen/scratchpad/test_print_label', info)
