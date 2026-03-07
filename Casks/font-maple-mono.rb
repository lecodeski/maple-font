cask "font-maple-mono-custom" do
  version "7.8"
  sha256 :no_check

  url "https://github.com/lecodeski/homebrew-maple-font/releases/download/v-latest/MapleMono-NF.zip"
  name "Maple Mono NF"
  desc "Forked build of Maple Mono with Nerd Font icons"
  homepage "https://github.com/lecodeski/homebrew-maple-font"

  font "MapleMono-NF-Regular.ttf"
  font "MapleMono-NF-Bold.ttf"
  font "MapleMono-NF-Italic.ttf"
  font "MapleMono-NF-BoldItalic.ttf"
end
