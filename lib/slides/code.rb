class Code
  def self.highlight(code, lexer: :python)
    Pygments.highlight(code, lexer: lexer)
  end
end
