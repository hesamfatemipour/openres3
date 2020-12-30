local http = require"socket.http"
local ltn12 = require"ltn12"

local _MIDDLEWARE = {}


-- request variables
local MIDDLEWARE_HOST = '10.0.1.12'
local MIDDLEWARE_PORT = '5000'

-- encodes the url into string
function urlencoded(s)
  s = s:gsub('+', ' ')
       :gsub('%%(%x%x)', function(h)
                         return string.char(tonumber(h, 16))
                         end)
  return s
end

-- parses the url params in request url
function _MIDDLEWARE.pars_url(url)
  s = s:match('%s+(.+)')

  local params = {}
  for k,v in s:gmatch('([^&=?]-)=([^&=?]+)') do
    params[ k ] = urlencoded(v)
  end
  return params
end

--handles talking to middleware
function _MIDDLEWARE.talk_to_middleware(user_id, bucket_name)

    local url = string.format("%s:%s/users/%s?bucket_name=%s", MIDDLEWARE_HOST, MIDDLEWARE_PORT, user_id, bucket_name)

    local result, resp_status_code, resp_headers, resp_status = http.request {
        method = "POST",
        url = url,
        headers = {
            ["Content-Type"] = "text/plain",
        },
    }

    if resp_status_code == 200 then
        can_create = true
    else
        can_create = false
    end

    return can_create
end

return _MIDDLEWARE