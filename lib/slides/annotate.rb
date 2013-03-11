# encoding: utf-8
class Annotate < Slim::Filter
  def on_slim_embedded(engine, body)
    code = Slim::CollectText.new.call(body)
    code = annotate code
    html = Albino.colorize code, :python

    [:static, html]
  end

  private

  def annotate(input)
    Annotator.new(input).execute
  end
end
