__module_name__ = "Marius survey script" 
__module_version__ = "1.0.0" 
__module_description__ = "Auto answer" 

print "\0034",__module_name__, __module_version__,"has been loaded\003"
import re
import csv
import xchat
import Levenshtein

def on_message(data, something, somethingb):
    nick = data[0]
    message = data[1]
    
    answers = csv.reader(open('/home/mariuskde/workspace/viktorina/viktorina_uniq_printable.txt', 'r'))

    if (nick == "Anna" or nick == "mar"):
        match = re.match(".*[0-9]+th Quiz Question:\x02 (.*)$", message)
        if (match):
            question = match.group(1).replace("\xc2\xa0", " ").upper()
            best_ratio = 0.0
            best_answer = None
            for row in answers:
                test_answer, test_question = row
                ratio = Levenshtein.ratio(test_question, question)
                if ratio > best_ratio:
                    best_ratio = ratio
                    best_answer = row

            print "Answer: %s (%s) q: %s" % (best_answer[0], best_ratio, best_answer[1])
#            if best_ratio > 0.80:
#                xchat.get_context().command("say %s" % (best_answer[0].lower()))
                 
xchat.hook_print('Channel Message', on_message)
