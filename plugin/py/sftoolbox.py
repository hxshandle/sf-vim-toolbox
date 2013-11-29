try:
  import vim
  import sys,os,subprocess
  import ConfigParser

  home_dir = os.getenv('HOME')
  sfconf_file = os.path.join(home_dir,'.sfconf')
  has_sfconf = os.path.isfile(sfconf_file)
  cfg = ConfigParser.SafeConfigParser()
  # scss mapping dirs dict
  scss_dict={}
  if has_sfconf:
    cfg.read(sfconf_file)
    if cfg.has_section('scss'):
      scsslist = cfg.items('scss')
      for k,v in scsslist:
        p = v.split(":")
        scss_dict[p[0]]=p[1]
      #print scss_dict



  def sf_process_scss():
    #cbf = current buffer file
    cbf = vim.current.buffer.name
    #cbd = current buffer dir
    cbd = os.path.dirname(cbf)
    base_name = os.path.basename(cbf)
    if cbd in scss_dict:
      try:
        dict_path = os.path.join(scss_dict[cbd],base_name[0:-5]+".css")
        subprocess.check_call(['sass',cbf,dict_path])
      except OSError as e:
        print e


  def sf_demo():
    print "sf demo 1"

  def _cfg_err():
    print "File '.sfconf' error or not found"


  def sf_main():
    if not has_sfconf:
      _cfg_err();
      return


  sf_main()
  #sf_process_scss()

except OSError as e:
  print e
