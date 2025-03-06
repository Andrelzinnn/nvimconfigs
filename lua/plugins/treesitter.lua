return {
  "nvim-treesitter/nvim-treesitter",
  build = ":TSUpdate",
  config = function()
      local config = require("nvim-treesitter.configs")
      config.setup({
        ensure_installed = {
          "python",
          "java",
          "javascript",
          "css",
          "c",
          "lua",
          "vim",
          "vimdoc",
          "query",
          "markdown"
        },
        sync_install = false,
        auto_install = true,
        highlight = { enable = true },
        indent = { enable = true }
      })
  end
}
