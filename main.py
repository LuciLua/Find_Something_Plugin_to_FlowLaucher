
import sys,os
parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher, FlowLauncherAPI
import subprocess


audios = 'ext:aac;ac3;aif;aifc;aiff;au;cda;dts;fla;flac;it;m1a;m2a;m3u;m4a;m4b;m4p;mid;midi;mka;mod;mp2;mp3;mpa;ogg;ra;rmi;snd;spc;umx;voc;wav;wma;xm'
compacteds = 'ext:7z;ace;arj;bz2;cab;gz;gzip;jar;r00;r01;r02;r03;r04;r05;r06;r07;r08;r09;r10;r11;r12;r13;r14;r15;r16;r17;r18;r19;r20;r21;r22;r23;r24;r25;r26;r27;r28;r29;rar;tar;tgz;z;zip'
documents = 'ext:c;chm;cpp;csv;cxx;doc;docm;docx;dot;dotm;dotx;h;hpp;htm;html;hxx;ini;java;lua;mht;mhtml;odt;pdf;potx;potm;ppam;ppsm;ppsx;pps;ppt;pptm;pptx;rtf;sldm;sldx;thmx;txt;vsd;wpd;wps;wri;xlam;xls;xlsb;xlsm;xlsx;xltm;xltx;xml'
executables = 'ext:bat;cmd;exe;msi;msp;scr'
folders = 'folder:'
images = 'ext:ani;bmp;gif;ico;jpe;jpeg;jpg;pcx;png;psd;tga;tif;tiff;webp;wmf'
videos = 'ext:3g2;3gp;3gp2;3gpp;amr;amv;asf;avi;bdmv;bik;d2v;divx;drc;dsa;dsm;dss;dsv;evo;f4v;flc;fli;flic;flv;hdmov;ifo;ivf;m1v;m2p;m2t;m2ts;m2v;m4v;mkv;mp2v;mp4;mp4v;mpe;mpeg;mpg;mpls;mpv2;mpv4;mov;mts;ogm;ogv;pss;pva;qt;ram;ratdvd;rm;rmm;rmvb;roq;rpm;smil;smk;swf;tp;tpr;vob;vp6;webm;wm;wmp;wmv'



def copy2clip(palavras):
    """Put translation into clipboard."""
    
    termo = palavras.split()
    
    type = termo[0] 
    input_search = termo[1] 
    
    result = ""
    
    if type == "all":
        result = f"{input_search}"
    if type == "a":
        result = f"{audios} {input_search}"
    if type == "c":
        result = f"{compacteds} {input_search}"
    if type == "d":
        result = f"{documents} {input_search}"
    if type == "e":
        result = f"{executables} {input_search}"
    if type == "f":
        result = f"{folders} {input_search}"
    if type == "i":
        result = f"{images} {input_search}"
    if type == "v":
        result = f"{videos} {input_search}"
    
    cmd = 'echo '+result.strip()+'|clip'
    
    return subprocess.check_call(cmd, shell=True)


DEFAULT_SEARCH_LIMIT = 10

class ExecuteFind(FlowLauncher):
    
    
    def search(self, query):
        return[{
            "Title": "missing argument...",
            "SubTitle": "'a' - audio \n 'c' - zips \n 'd' - documents",
            "IcoPath": "Images/app.png",
        }]

    def query(self, query): 
        words = query.split()
        
    
        if len(words) < 2:
            return[{
                "Title": "missing argument... [type] + [name]",
                "SubTitle": "types: 'a' - audio | 'c' - zips | 'd' - documents 'e' - executables \n 'f' - folders | 'i' - images | 'v' - videos",
                "IcoPath": "Images/app.png",
            }]
        else:
            primeira_palavra = words[0]
            segunda_palavra = words[1]
            palavras = query
            
            # self.add_item({"Title": 'ásd', "Subtitle": "Subtitlessad"})
            # self.add_item({"Title": 'ásd', "Subtitle": "Subasdtitlessad"})
            # self.add_item({"Title": 'ásd', "Subtitle": "Subtitldessad"})
            
            
            return [
                {
                    "Title": "type: {0} | word: {1}".format(primeira_palavra, segunda_palavra),
                    "SubTitle": "Press to search now.",
                    "IcoPath": "Images/app.png",
                    "JsonRPCAction": {
                        "method": "copy",
                        "parameters": [palavras]
                    }
                }
            ]
        
        
        
    def copy(self, palavras):
        """Copy translation to clipboard."""
        FlowLauncherAPI.show_msg("Copied to clipboard", copy2clip(palavras))
    

if __name__ == "__main__":
    ExecuteFind()