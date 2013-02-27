# encoding: utf-8
class Annotate < Slim::Filter
  def on_slim_embedded(engine, body)
    code = Slim::CollectText.new.call(body)
    # code = annotate code
    html = Albino.colorize code, :python

    [:static, html]
  end

  private

  def annotate(input)
    input = input.gsub /^(.*) #!$/, '(\1) rescue $!.class # =>'
    input = input.gsub('"', "'")
    output = `python -c "#{input}"`

    output = output.gsub /^\((.*)\) rescue \$!\.class # =>\s*(.*)$/, '\1 # error: \2'
    output = output.gsub /# +=> (.*)/, '# \1'
    output
  end
end
