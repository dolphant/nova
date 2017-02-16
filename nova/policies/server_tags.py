# Copyright 2016 Cloudbase Solutions Srl
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_policy import policy

from nova.policies import base


POLICY_ROOT = 'os_compute_api:os-server-tags:%s'


server_tags_policies = [
    base.create_rule_default(
        POLICY_ROOT % 'delete_all',
        base.RULE_ANY,
        "Delete all the server tags",
        [
            {
                'method': 'DELETE',
                'path': '/servers/{server_id}/tags'
            }
        ]),
    base.create_rule_default(
        POLICY_ROOT % 'index',
        base.RULE_ANY,
        "List all tags for given server",
        [
            {
                'method': 'GET',
                'path': '/servers/{server_id}/tags'
            }
        ]),
    base.create_rule_default(
        POLICY_ROOT % 'update_all',
        base.RULE_ANY,
        "Replace all tags on specified server with the new set of tags.",
        [
            {
                'method': 'PUT',
                'path': '/servers/{server_id}/tags'

            }
        ]),
    base.create_rule_default(
        POLICY_ROOT % 'delete',
        base.RULE_ANY,
        "Delete a single tag from the specified server",
        [
            {
                'method': 'DELETE',
                'path': '/servers/{server_id}/tags/{tag}'
            }
        ]
    ),
    base.create_rule_default(
        POLICY_ROOT % 'update',
        base.RULE_ANY,
        "Add a single tag to the server if server has no specified tag",
        [
            {
                'method': 'PUT',
                'path': '/servers/{server_id}/tags/{tag}'
            }
        ]
    ),
    base.create_rule_default(
        POLICY_ROOT % 'show',
        base.RULE_ANY,
        "Check tag existence on the server.",
        [
            {
                'method': 'GET',
                'path': '/servers/{server_id}/tags/{tag}'
            }
        ]
    ),
    policy.RuleDefault(
        name=POLICY_ROOT % 'discoverable',
        check_str=base.RULE_ANY),
]


def list_rules():
    return server_tags_policies
